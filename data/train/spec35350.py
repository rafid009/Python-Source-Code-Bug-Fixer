import numpy as np 

def function(x):

	r6 = 3
	f5 = x
	paths = []
	try:
		if r6 < 0:
			f5 = f5/r6
			f5 = f5+7
			paths.append(1)
		else:
			r6 = f5/r6
			r6 = 5-x
			x = r6-1
			paths.append(2)
		if x > 7:
			f5 = r6/8
			r6 = r6+5
			f5 = f5*x
			paths.append(3)
		else:
			r6 = r6+r6
			f5 = f5+9
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))