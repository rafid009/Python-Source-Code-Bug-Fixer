import numpy as np 

def function(x):

	t8 = x
	i9 = x
	x = 5
	paths = []
	try:
		if t8 >= 8:
			x = x*0
			paths.append(1)
		else:
			i9 = 9*i9
			paths.append(2)
		if x < 4:
			i9 = i9-4
			paths.append(3)
		else:
			t8 = t8-9
			x = 6*x
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		t8 = i9**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))