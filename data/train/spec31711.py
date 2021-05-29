import numpy as np 

def function(x):

	l7 = x
	t7 = x
	x = x
	paths = []
	try:
		if l7 <= 7:
			x = x+7
			paths.append(1)
		else:
			x = 3*5
			x = 2+4
			t7 = 7/7
			paths.append(2)
		if x <= 4:
			x = t7+0
			x = 3*l7
			paths.append(3)
		else:
			t7 = t7+7
			l7 = l7/9
			x = 2-5
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