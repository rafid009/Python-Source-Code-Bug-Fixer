import numpy as np 

def function(x):

	v9 = x
	j8 = 2
	paths = []
	try:
		if x < 0:
			j8 = 5+x
			x = x*v9
			j8 = j8/6
			paths.append(1)
		else:
			x = x*9
			v9 = v9*4
			x = x-v9
			paths.append(2)
		if x > 1:
			j8 = 6+8
			x = x+x
			j8 = 7/v9
			paths.append(3)
		else:
			x = x+3
			x = x/7
			x = 9+j8
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		j8 = v9**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))