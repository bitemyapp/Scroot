#       Scroot Readme


Django auditing / change + timestamp logging for the dreadfully lazy.

##	Why?

Because not everyone has access to a database with native transactions and
thus cannot use the apps that assume db.transaction that all the cool kids
are deploying.

I didn't want to inject a bunch of arbitrary "log when this happens with a 
timestamp" lines of code into my projects. Bleedin' stupid.

Also, this is easy as a water slide to deploy and doesn't require migrating 
all of your databases from MyISAM to InnoDB because of forerunner myopia.

##	What?

Some people use MyISAM. No, I don't get it either. If Alex ever finishes the MongoDB 
backend for Django, this might be helpful for that too.

I'm uncertain of the performance implications. It was designed for a schema that separated 
the high read/low write/high value fields from the high-write-rate fields. If
you don't know what normalization is, all hope is lost.

##	Scroot?

Auditing => scrutiny => scroot

Yeah it's dumb, but it's not a real word and I like it. Say it out loud, it'll
grow on you. It turns my projects into fuzzy pets for me.

##	How?

Very carefully. I'm still using threadlocals and there are literally no tests.
I might make it thread-safe soon but you're kidding yourself if you think I
wrote this because I felt the need to make an obscenely dirty and low LOC
auditing app with lots of unit tests.

Add a tuple to your settings.py that looks something like this,

	# left side app, right side model. cool beans eh?
	AUDITED_MODELS = (
	                    ('auth', 'user'),
	                    ('accounting', 'Company'), 
	                    ('accounting', 'WhoCares'),
	                    ('accounting', 'Transaction'),
	                    ('merch', 'Product')
	                 )

And add:
	'scroot.middleware.threadlocals.ThreadLocals',

To your middleware tuple.

As long as Django knows where your app is, you should be in good shape. 
If this breaks, your path is scrambled worse than hangover eggs. 

Go fix it.

Don't blame my impeccable abuse of undocumented django functions.
