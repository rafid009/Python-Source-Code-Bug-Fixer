import numpy as np 

def function(x):

	i0 = x
	u1 = 4
	paths = []
	try:
		if x <= 8:
			u1 = u1*0
			x = x-5
			i0 = i0-2
			paths.append(1)
		else:
			u1 = u1+7
			i0 = 3*i0
			paths.append(2)
		if i0 > 2:
			i0 = x*i0
			x = x/7
			i0 = u1/i0
			paths.append(3)
		else:
			i0 = 9*x
			u1 = i0*u1
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))