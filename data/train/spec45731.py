import numpy as np 

def function(x):

	j4 = x
	f2 = x
	paths = []
	try:
		if f2 <= 6:
			f2 = x*f2
			f2 = j4+f2
			paths.append(1)
		else:
			f2 = f2/4
			paths.append(2)
		if j4 < 7:
			x = j4-x
			x = x+0
			paths.append(3)
		else:
			f2 = f2*8
			f2 = 5/f2
			f2 = 1/f2
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))