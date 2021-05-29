import numpy as np 

def function(x):

	t5 = 2
	v1 = x
	paths = []
	try:
		if v1 >= 9:
			t5 = t5-7
			v1 = v1/v1
			x = x+3
			paths.append(1)
		else:
			t5 = 3/t5
			paths.append(2)
		if v1 <= 8:
			t5 = v1-8
			t5 = t5-v1
			paths.append(3)
		else:
			x = x/6
			t5 = t5+v1
			x = t5/2
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))