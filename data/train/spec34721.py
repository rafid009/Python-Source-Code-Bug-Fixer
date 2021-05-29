import numpy as np 

def function(x):

	o5 = x
	l9 = 3
	paths = []
	try:
		if x <= 4:
			o5 = 9-9
			l9 = l9+9
			l9 = l9+1
			paths.append(1)
		else:
			o5 = o5+9
			l9 = l9-o5
			paths.append(2)
		if o5 < 8:
			x = 0/4
			o5 = o5-0
			l9 = l9+2
			paths.append(3)
		else:
			o5 = 4*o5
			o5 = o5+l9
			x = x+l9
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))