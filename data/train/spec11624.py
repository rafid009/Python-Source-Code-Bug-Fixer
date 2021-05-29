import numpy as np 

def function(x):

	b6 = x
	k2 = 3
	paths = []
	try:
		if b6 < 8:
			x = 3+4
			k2 = 6/b6
			b6 = b6/8
			paths.append(1)
		else:
			b6 = k2+b6
			x = 2/k2
			paths.append(2)
		if b6 >= 2:
			k2 = k2+1
			b6 = b6+5
			paths.append(3)
		else:
			x = 4*0
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))