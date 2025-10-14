namespace cpp save_service

service Save{
	# uername: 访问myserver的用户名称
	# password: myserver的密码的md5sum的前8位
	# 用户名密码验证成功会返回0，验证失败会返回1
	# 验证成功后，结果会被保存到myserver:homework/lesson_6/result.txt中
    # 此为save服务的客户端，所以生成到match_system里，并且同match_service一样集成到main里
	i32 save_data(1: string username, 2: string password, 3: i32 player1_id, 4: i32 player2_id)
}
