import numpy as np 

def function(x):

	b6 = x
	t7 = 5
	paths = []
	try:
		if b6 < 7:
			x = 4-b6
			paths.append(1)
		else:
			x = 6*x
			b6 = 1-x
			x = x/3
			paths.append(2)
		if x <= 9:
			t7 = 0-9
			t7 = 1+8
			t7 = t7+7
			paths.append(3)
		else:
			b6 = 3+x
			t7 = t7*1
			x = x/9
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		t7 = b6**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))