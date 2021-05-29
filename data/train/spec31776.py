import numpy as np 

def function(x):

	f6 = x
	l0 = 2
	paths = []
	try:
		if l0 >= 8:
			l0 = 7*l0
			x = x-0
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if l0 > 0:
			f6 = f6/8
			l0 = l0*0
			x = x+1
			paths.append(3)
		else:
			l0 = 9-l0
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		l0 = f6**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))