import numpy as np 

def function(x):

	j9 = x
	i2 = x
	paths = []
	try:
		if x >= 8:
			i2 = 5*2
			i2 = i2-5
			x = 0-x
			paths.append(1)
		else:
			i2 = 2*0
			paths.append(2)
		if i2 > 7:
			j9 = 5/2
			x = x+4
			i2 = x/2
			paths.append(3)
		else:
			i2 = x*i2
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		i2 = j9**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))