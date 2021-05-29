import numpy as np 

def function(x):

	i2 = 5
	r5 = x
	paths = []
	try:
		if x < 9:
			r5 = 7*r5
			paths.append(1)
		else:
			i2 = i2+6
			r5 = r5*1
			paths.append(2)
		if r5 <= 6:
			i2 = 5+i2
			r5 = 3/1
			paths.append(3)
		else:
			r5 = x-1
			r5 = r5-8
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		x = r5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))