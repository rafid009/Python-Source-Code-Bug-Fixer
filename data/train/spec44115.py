import numpy as np 

def function(x):

	j3 = 3
	i8 = 2
	paths = []
	try:
		if x < 1:
			x = 5*x
			j3 = j3+i8
			j3 = j3/7
			paths.append(1)
		else:
			i8 = i8+i8
			x = 4+1
			x = 8+x
			paths.append(2)
		if i8 <= 3:
			x = x*i8
			i8 = 7-j3
			i8 = i8*4
			paths.append(3)
		else:
			i8 = 4*i8
			j3 = 5-0
			i8 = 8/i8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))