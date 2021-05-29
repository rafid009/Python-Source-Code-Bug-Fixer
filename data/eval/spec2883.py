import numpy as np 

def function(x):

	e6 = x
	f5 = x
	paths = []
	try:
		if f5 >= 4:
			f5 = f5+9
			f5 = 3+f5
			x = x+e6
			paths.append(1)
		else:
			e6 = 2*2
			e6 = e6/5
			e6 = e6/1
			paths.append(2)
		if e6 < 5:
			e6 = e6+7
			e6 = 4-e6
			x = 0*x
			paths.append(3)
		else:
			x = 9/8
			x = 7+6
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))