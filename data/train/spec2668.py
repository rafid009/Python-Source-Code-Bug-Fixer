import numpy as np 

def function(x):

	k7 = 9
	i8 = x
	paths = []
	try:
		if k7 >= 7:
			x = k7*k7
			k7 = x*k7
			paths.append(1)
		else:
			x = x*6
			k7 = i8+k7
			x = x-1
			paths.append(2)
		if x < 3:
			x = k7*0
			paths.append(3)
		else:
			k7 = k7-5
			k7 = k7*9
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		k7 = i8**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))