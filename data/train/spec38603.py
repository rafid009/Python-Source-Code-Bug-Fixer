import numpy as np 

def function(x):

	t6 = 0
	u7 = x
	x = x
	paths = []
	try:
		if x <= 8:
			u7 = u7*0
			x = x/1
			paths.append(1)
		else:
			u7 = u7+x
			paths.append(2)
		if x < 1:
			t6 = 6*x
			paths.append(3)
		else:
			u7 = t6-8
			x = x+u7
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))