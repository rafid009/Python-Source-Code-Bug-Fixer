import numpy as np 

def function(x):

	t3 = 9
	t7 = x
	paths = []
	try:
		if t3 < 4:
			t3 = t3*t3
			paths.append(1)
		else:
			t3 = t3*7
			t3 = t3/5
			t3 = 0-t3
			paths.append(2)
		if x < 0:
			t3 = t3*x
			x = 4+x
			x = 1*0
			paths.append(3)
		else:
			t7 = 2*6
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		t7 = t7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))