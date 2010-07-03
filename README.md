#	Scroot Readme

Django auditing for the terminally lazy.

##	Why?

Because not everyone has access to a database with native transactions.

##	What?

Yeah, Some people use ISAM. No, I don't get it either. If Alex ever finishes
the MongoDB backend for Django, this might be helpful for that too. 

I'm uncertain of the performance implications. It was designed for a schema 
that separated the high read/write ratio fields from the high-write-rate fields.

##	Scroot?

Auditing => scrutiny => scroot

Yeah it's dumb, but it's not a real word and I like it.

##	How?

Very carefully. I'm still using threadlocals and there are literally no tests.

Add a tuple to your settings.py that looks something like this,

	# left side app, right side model. cool beans eh?
	AUDITED_MODELS = (
	                    ('auth', 'user'),
	                    ('accounting', 'Company'), 
	                    ('accounting', 'WhoCares'),
	                    ('accounting', 'Transaction'),
	                    ('merch', 'Product')
	                 )

As long as Django knows where your app is, you should be in good shape. 
If this breaks, your path is scrambled worse than hangover eggs. Go fix it.