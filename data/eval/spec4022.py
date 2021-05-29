import numpy as np 

def function(x):

	f9 = 9
	j6 = 5
	paths = []
	try:
		if j6 <= 2:
			j6 = 2-3
			f9 = 7/f9
			f9 = 7-2
			paths.append(1)
		else:
			j6 = j6+1
			j6 = j6*1
			f9 = f9+f9
			paths.append(2)
		if x <= 9:
			j6 = 4-j6
			x = f9*3
			x = x-0
			paths.append(3)
		else:
			f9 = f9/x
			x = f9/j6
			j6 = 8+j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		j6 = j6**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))