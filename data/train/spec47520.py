import numpy as np 

def function(x):

	t7 = x
	j2 = x
	paths = []
	try:
		if x < 5:
			j2 = x/7
			x = x+t7
			paths.append(1)
		else:
			j2 = j2/2
			x = 4-x
			j2 = 6*6
			paths.append(2)
		if j2 >= 1:
			t7 = 1*1
			x = 8*x
			paths.append(3)
		else:
			x = x*7
			j2 = j2+j2
			x = t7-x
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		j2 = t7**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))