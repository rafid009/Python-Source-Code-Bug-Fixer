import numpy as np 

def function(x):

	v0 = x
	l9 = x
	paths = []
	try:
		if l9 < 8:
			l9 = 0*l9
			x = x/v0
			x = x+x
			paths.append(1)
		else:
			l9 = l9/8
			paths.append(2)
		if x > 4:
			l9 = 4-l9
			v0 = 0-v0
			x = v0/v0
			paths.append(3)
		else:
			l9 = x+x
			l9 = 3-l9
			l9 = 8+l9
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		v0 = l9**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))