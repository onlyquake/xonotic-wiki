New QC Syntax
=============

It is possible that at some point we decide to switch QC-compiler which requires some changes to the code.

~~For more information see http://dev.xonotic.org/projects/bocc~~

(Update: Blub's bocc compiler didn't make it, but someone else came along, both devs [joined forces](https://github.com/graphitemaster/gmqcc/graphs/contributors) and brought us [GMQCC](https://graphitemaster.github.io/gmqcc/doc.html).
 This is now the QuakeC compiler used by the Xonotic project.)

Clean syntax:
-------------

In fteqcc there are some ambiguities regarding fieldpointers, function pointers, and field-return-types etc.
A clean syntax is needed, the current implementation uses the following:

|definition|meaning|
|----------|-------|
|`float foo`|global variable|
|`float .foo`|entity field|
|`.float foo`|fieldpointer|
|`.float .foo`|entity field of type fieldpointer|
|`float foo(void)`|function|
|`float foo*(void)`|function pointer|
|`.float foo(void)`|function returning a fieldpointer .float|
|`.float foo*(void)`|function pointer, returning a fieldpointer .float|
|`float .foo(void)`|entity field of type function returning float|
|`.float .foo(void)`|entity field of type function returning fieldpointer|

Function definitions:
---------------------

The old-style QC way of defining functions will not be supported, so

    void(float x) something = { ... }

becomes

    void something(float x) { ... }

which is the most common way to define functions in the xonotic code already anyway.

Constants:
----------

From now on, the code

    float x = 3

does what the first instinct tells you: it creates a global with the initial value 3. Contrary to old QC, where it created a constant.
To create a constant use:

    const float x = 3

Extendable functions:
---------------------

Since menuQC has some funny macro: ACCUMULATE\_FUNCTIONS, it seemed like a nice syntactical sugar to allow the following:

    float myfunc() extendable
    {
        float mylocal = 3;
    }

    /* other code */

    float myfunc()
    {
        mylocal += 5;
        if (mylocal > 20)
            return mylocal;
    }

    /* optionally: */
    float myfunc() final
    {
        return 3;
    }

Variadic parameters (do not use yet)
------------------------------------

(This might get changed to be more flexible so do not rely on this syntax…)

Another “enhancement” is the possibility to have functions with variadic parameter lists. However, the only way to sanely access them (until pointers are allowed) is via a recursive way.
Here’s an example that assumes float parameters and prints them one after the other:

    void printfloats(float count, float first, ...)
    {
        if (count <= 0) // if there are no parameters, return
            return;
        if (count == 1) { // If there's one parameter, print it, plus a new-line
            print(strcat(ftos(first), "\n"));
            return;
        }
        // Otherwise we have multiple parameters left, so print the float, and add a comma
        print(strcat(ftos(first), ", "));
        myprint(count-1, ...);
    }

So `myprint(4, 1, 2, 3, 4)` would print "1, 2, 3, 4\\n"

