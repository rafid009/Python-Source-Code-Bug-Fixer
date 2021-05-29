import numpy as np 

def function(x):

	h7 = 2
	j3 = x
	paths = []
	try:
		if x <= 8:
			h7 = h7*1
			x = x/9
			h7 = h7/x
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if j3 >= 3:
			h7 = x-j3
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j3 = j3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))