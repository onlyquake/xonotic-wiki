TrackerWorkflow
===============

THIS IS NOT TRUE ON THIS TRACKER YET
====================================

Status "new"
------------

Items are in status "new" if they are posted and not yet verified.

From there, the statuses "feedback", "rejected", and "verified" can be entered.

Status "feedback"
-----------------

The item is waiting for a reply from the original submitter, on which depends whether it can be accepted.

In the special case of patches, this state is also used after a failed code review.

From here, the status "new" is entered after a reply by the original submitter.

Status "rejected"
-----------------

The bug cannot be reproduced or is not a bug. / The feature is not wanted. / The patch is not wanted.

The item is closed.

Status "verified"
-----------------

The bug could be reproduced. / The feature would be a good idea. / The patch applies and a short test showed that it seems to work.

From here, the status "assigned" can be entered.

Status "assigned"
-----------------

The bug has been assigned to someone who can fix it. / The feature is assigned to someone who can implement it. / The patch is assigned to someone who can review it.

From here, the status "resolved" or "wontfix" can be entered. As a special case, patches can go to a status "feedback and assigned" if the reviewer has an open issue with the patch.

Status "resolved"
-----------------

The bug has been fixed in svn. / The feature has been implemented in svn.

Status "wontfix"
----------------

The bug won't be fixed due a fix breaking other intended behaviour or being impossible. / The feature appears to be out of scope. / The feature implemented by the patch is a security or other risk to the game and thus won't be applied.

Status "feedback and assigned"
------------------------------

Like feedback, but it can be moved to "assigned" instead of "new".

Status "closed"
---------------

The issue has been closed for another reason and cannot be reopened.

User permissions
----------------

Reporters can go from any closing state, and from state "feedback", to status "new". They also can go from "feedback and assigned" back to status "assigned". Otherwise they cannot change status.

Contributors can perform the whole workflow, except they cannot move anything to status "closed", "wontfix" or "resolved" (as they also have no svn commit access).

Developers can perform the whole workflow.

Managers can circumvent workflow restrictions.
