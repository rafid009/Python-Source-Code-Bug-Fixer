import numpy as np 

def function(x):

	t6 = x
	j7 = x
	paths = []
	try:
		if x >= 7:
			j7 = j7/1
			t6 = 8+t6
			paths.append(1)
		else:
			j7 = t6*j7
			paths.append(2)
		if t6 <= 3:
			x = t6*1
			j7 = 2-j7
			x = x*t6
			paths.append(3)
		else:
			j7 = 6+t6
			x = x*2
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		j7 = t6**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))