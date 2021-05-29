import numpy as np 

def function(x):

	t6 = x
	m5 = x
	paths = []
	try:
		if t6 < 6:
			x = x/t6
			m5 = m5-m5
			m5 = m5/9
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if m5 > 0:
			t6 = 2/6
			m5 = m5-m5
			paths.append(3)
		else:
			m5 = 9*t6
			x = x+x
			t6 = t6-m5
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		m5 = t6**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))