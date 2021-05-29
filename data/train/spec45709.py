import numpy as np 

def function(x):

	o1 = 9
	i4 = 7
	paths = []
	try:
		if x >= 3:
			i4 = i4*3
			x = 5+x
			paths.append(1)
		else:
			i4 = i4*o1
			o1 = 1*0
			o1 = o1+6
			paths.append(2)
		if x <= 6:
			o1 = 4+7
			i4 = x/i4
			o1 = o1*x
			paths.append(3)
		else:
			o1 = i4-8
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		i4 = o1**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))