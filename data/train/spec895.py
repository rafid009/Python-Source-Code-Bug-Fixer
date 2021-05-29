import numpy as np 

def function(x):

	j3 = 8
	b4 = x
	paths = []
	try:
		if b4 < 9:
			x = x*1
			j3 = j3-8
			paths.append(1)
		else:
			x = x/j3
			paths.append(2)
		if j3 <= 5:
			b4 = 3-b4
			b4 = b4/1
			paths.append(3)
		else:
			b4 = b4-3
			x = x*1
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))