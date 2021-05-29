import numpy as np 

def function(x):

	i2 = 8
	j2 = x
	paths = []
	try:
		if x > 8:
			x = 2+5
			i2 = x/i2
			j2 = j2+7
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if x <= 6:
			j2 = 5/x
			i2 = i2/8
			paths.append(3)
		else:
			x = 6+i2
			j2 = j2-i2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		i2 = j2**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))