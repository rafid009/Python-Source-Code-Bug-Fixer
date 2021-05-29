import numpy as np 

def function(x):

	t1 = 7
	i2 = x
	paths = []
	try:
		if t1 > 7:
			i2 = i2+3
			i2 = i2*3
			paths.append(1)
		else:
			i2 = 1-i2
			t1 = 3-t1
			paths.append(2)
		if x < 3:
			t1 = i2*t1
			paths.append(3)
		else:
			x = t1*8
			x = x+t1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))