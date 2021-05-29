import numpy as np 

def function(x):

	t5 = 6
	j1 = x
	paths = []
	try:
		if x >= 1:
			t5 = 9*t5
			paths.append(1)
		else:
			t5 = x*1
			paths.append(2)
		if x < 4:
			x = j1/x
			x = j1-9
			x = 0*2
			paths.append(3)
		else:
			t5 = t5+1
			x = x+7
			t5 = j1/4
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		x = j1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))