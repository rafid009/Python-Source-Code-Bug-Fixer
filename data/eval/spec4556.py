import numpy as np 

def function(x):

	f2 = 7
	i2 = x
	paths = []
	try:
		if x > 2:
			x = x/x
			x = i2+f2
			f2 = 5/i2
			paths.append(1)
		else:
			f2 = i2+i2
			i2 = i2-1
			paths.append(2)
		if f2 <= 1:
			i2 = i2-7
			x = 6/8
			paths.append(3)
		else:
			i2 = i2/5
			f2 = 4/4
			f2 = f2+f2
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		i2 = f2**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))