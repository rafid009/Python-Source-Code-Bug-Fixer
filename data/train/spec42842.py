import numpy as np 

def function(x):

	f2 = 6
	l9 = x
	x = 6
	paths = []
	try:
		if x > 3:
			l9 = l9/x
			f2 = f2-l9
			paths.append(1)
		else:
			f2 = x/l9
			x = 7+5
			x = x+2
			paths.append(2)
		if l9 >= 9:
			l9 = 7/l9
			x = 9+8
			paths.append(3)
		else:
			f2 = l9+l9
			f2 = l9/l9
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		f2 = l9**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))