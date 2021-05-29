import numpy as np 

def function(x):

	k4 = x
	i5 = 2
	x = 1
	paths = []
	try:
		if i5 >= 9:
			k4 = i5-6
			i5 = i5/6
			i5 = i5/8
			paths.append(1)
		else:
			x = x+7
			x = x+1
			paths.append(2)
		if i5 < 8:
			i5 = 4+8
			x = i5*x
			k4 = 5/k4
			paths.append(3)
		else:
			k4 = x*2
			k4 = k4*1
			k4 = k4/3
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		k4 = k4**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))