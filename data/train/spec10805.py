import numpy as np 

def function(x):

	j8 = x
	t2 = x
	paths = []
	try:
		if x >= 6:
			j8 = x*x
			j8 = 0-j8
			t2 = t2-j8
			paths.append(1)
		else:
			j8 = 5-2
			j8 = x*x
			paths.append(2)
		if j8 > 5:
			t2 = t2/7
			t2 = 5/9
			x = t2+7
			paths.append(3)
		else:
			t2 = 7*t2
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		j8 = j8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))