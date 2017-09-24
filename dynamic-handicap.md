This mutator changes the handicap of players based on difference of their score to the mean score. Linear handicap value is calculated using the following formula:

	linear_handicap = |(score - mean) * g_dynamic_handicap_scale| ^ g_dynamic_handicap_exponent

After that the sign is restored and final handicap if calculated using this formula:

	if (linear_handicap >= 0)
	{
		handicap = linear_handicap + 1;
	}
	else
	{
		handicap = 1 / (|linear_handicap| + 1);
	}

## Server settings

	g_dynamic_handicap 0 "Whether to enable dynamic handicap."
	g_dynamic_handicap_scale 0.2 "The scale of the handicap. Larger values mean more penalties for strong players and more buffs for weak players."
	g_dynamic_handicap_exponent 1 "The exponent used to calculate handicap. 1 means linear scale. Values more than 1 mean stronger non-linear handicap. Values less than 1 mean weaker non-linear handicap"
	g_dynamic_handicap_min 0 "The minimum value of the handicap."
	g_dynamic_handicap_max 0 "The maximum value of the handicap."