import numpy as np 

def function(x):

	i9 = 4
	t5 = 1
	paths = []
	try:
		if t5 > 1:
			t5 = i9+t5
			paths.append(1)
		else:
			t5 = t5*i9
			i9 = 8+x
			paths.append(2)
		if i9 < 0:
			x = 8/x
			t5 = t5/3
			i9 = i9*6
			paths.append(3)
		else:
			x = x+x
			x = x+7
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		t5 = i9**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))