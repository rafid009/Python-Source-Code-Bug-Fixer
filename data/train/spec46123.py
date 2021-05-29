import numpy as np 

def function(x):

	j9 = 4
	f4 = 8
	paths = []
	try:
		if j9 < 3:
			x = 9-j9
			f4 = j9+5
			j9 = x-9
			paths.append(1)
		else:
			f4 = x+f4
			f4 = x-f4
			j9 = j9+x
			paths.append(2)
		if x >= 7:
			j9 = j9/3
			j9 = 2*j9
			f4 = 7-f4
			paths.append(3)
		else:
			f4 = x+2
			x = f4+7
			f4 = x+f4
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j9 = j9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))