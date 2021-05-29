import numpy as np 

def function(x):

	i2 = x
	w2 = x
	paths = []
	try:
		if i2 >= 7:
			w2 = w2/6
			i2 = x-4
			i2 = 9/5
			paths.append(1)
		else:
			w2 = w2*2
			w2 = w2-7
			w2 = 0+w2
			paths.append(2)
		if x >= 6:
			w2 = 3+6
			w2 = w2/7
			x = x-6
			paths.append(3)
		else:
			i2 = 8+i2
			w2 = 5+i2
			i2 = i2*6
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