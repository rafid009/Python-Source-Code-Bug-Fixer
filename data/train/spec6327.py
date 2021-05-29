import numpy as np 

def function(x):

	u1 = 5
	o2 = x
	paths = []
	try:
		if u1 >= 4:
			u1 = o2+x
			paths.append(1)
		else:
			o2 = 1*o2
			paths.append(2)
		if u1 >= 8:
			u1 = u1-3
			o2 = o2*7
			paths.append(3)
		else:
			o2 = 4*2
			u1 = u1/6
			o2 = o2*x
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		u1 = o2**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))