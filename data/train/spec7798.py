import numpy as np 

def function(x):

	j5 = x
	u5 = x
	paths = []
	try:
		if x <= 7:
			u5 = 4/u5
			u5 = u5/u5
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if j5 > 7:
			u5 = j5+u5
			j5 = j5-x
			paths.append(3)
		else:
			j5 = 8*4
			u5 = u5+2
			j5 = x-j5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		u5 = j5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))