import numpy as np 

def function(x):

	t7 = x
	j6 = 6
	paths = []
	try:
		if x < 0:
			t7 = t7+0
			t7 = 7/t7
			paths.append(1)
		else:
			t7 = t7/t7
			x = 9+x
			paths.append(2)
		if t7 >= 7:
			x = j6*x
			t7 = 5/t7
			j6 = 4+9
			paths.append(3)
		else:
			t7 = 8+x
			x = t7*2
			j6 = t7/3
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))