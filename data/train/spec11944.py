import numpy as np 

def function(x):

	j6 = 6
	b3 = x
	paths = []
	try:
		if b3 < 3:
			j6 = j6-0
			b3 = b3/j6
			paths.append(1)
		else:
			b3 = x*j6
			j6 = j6/7
			paths.append(2)
		if j6 > 8:
			j6 = 1+x
			paths.append(3)
		else:
			j6 = 3/2
			b3 = b3/1
			x = j6-3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))