import numpy as np 

def function(x):

	k2 = x
	j8 = x
	x = x
	paths = []
	try:
		if j8 >= 1:
			k2 = k2-9
			paths.append(1)
		else:
			k2 = 7+5
			k2 = 4-0
			x = x+9
			paths.append(2)
		if x <= 9:
			j8 = j8-2
			k2 = 9*1
			paths.append(3)
		else:
			j8 = 2+j8
			x = k2*8
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		j8 = j8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))