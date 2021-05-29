import numpy as np 

def function(x):

	b9 = x
	j6 = 7
	paths = []
	try:
		if b9 > 9:
			x = x/9
			b9 = 4*6
			x = x+8
			paths.append(1)
		else:
			b9 = 3/9
			b9 = b9+0
			paths.append(2)
		if x > 4:
			x = x*0
			j6 = j6/j6
			x = x-1
			paths.append(3)
		else:
			j6 = 8+j6
			b9 = x*1
			x = x-2
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))