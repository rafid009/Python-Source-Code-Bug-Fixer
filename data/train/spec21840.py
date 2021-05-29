import numpy as np 

def function(x):

	f6 = x
	r6 = x
	paths = []
	try:
		if x > 8:
			f6 = 2-f6
			x = x-2
			r6 = r6+x
			paths.append(1)
		else:
			f6 = 1/6
			paths.append(2)
		if f6 > 6:
			f6 = f6*8
			r6 = 6+r6
			paths.append(3)
		else:
			x = 3-f6
			x = x*r6
			f6 = f6*3
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))