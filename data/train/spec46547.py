import numpy as np 

def function(x):

	j6 = x
	i8 = x
	paths = []
	try:
		if i8 < 0:
			x = 9*5
			x = 2+x
			paths.append(1)
		else:
			j6 = 8+x
			paths.append(2)
		if x > 8:
			i8 = 5/9
			x = 8+3
			x = x+0
			paths.append(3)
		else:
			x = i8+1
			x = j6*x
			x = x*x
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		i8 = j6**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))