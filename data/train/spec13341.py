import numpy as np 

def function(x):

	j8 = x
	t7 = 8
	paths = []
	try:
		if x < 2:
			t7 = t7-8
			j8 = j8-t7
			paths.append(1)
		else:
			t7 = 1/t7
			paths.append(2)
		if j8 > 5:
			j8 = 2/j8
			j8 = t7+t7
			t7 = t7-t7
			paths.append(3)
		else:
			x = x*1
			x = x+4
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		t7 = j8**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))