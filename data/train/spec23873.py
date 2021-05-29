import numpy as np 

def function(x):

	i2 = 2
	b8 = x
	paths = []
	try:
		if i2 > 8:
			x = 7+x
			paths.append(1)
		else:
			i2 = i2*0
			x = 3*5
			i2 = i2+9
			paths.append(2)
		if i2 < 8:
			i2 = 1+i2
			b8 = b8-x
			paths.append(3)
		else:
			i2 = 4-i2
			b8 = b8+8
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		i2 = i2**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))