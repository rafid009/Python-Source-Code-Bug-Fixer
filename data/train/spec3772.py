import numpy as np 

def function(x):

	j7 = 2
	f3 = x
	paths = []
	try:
		if j7 < 3:
			j7 = f3+4
			f3 = f3-9
			j7 = 3*j7
			paths.append(1)
		else:
			x = 9-f3
			j7 = j7*8
			x = x*x
			paths.append(2)
		if f3 > 5:
			f3 = f3-5
			j7 = 0+j7
			paths.append(3)
		else:
			x = 6/1
			f3 = f3-x
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		j7 = j7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))