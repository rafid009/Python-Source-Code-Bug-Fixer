import numpy as np 

def function(x):

	r8 = x
	l4 = 4
	paths = []
	try:
		if l4 < 5:
			x = x+4
			l4 = 5-4
			l4 = r8-l4
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if l4 > 3:
			r8 = 4-6
			r8 = 5*2
			l4 = x+l4
			paths.append(3)
		else:
			l4 = r8/l4
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		l4 = r8**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))