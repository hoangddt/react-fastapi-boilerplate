SERVER?=inter.vn01
WORKING_DIR=/etc/nginx/
LET_ENCRYPT_WORKING_DIR=/etc/letsencrypt/
TODAY=$(shell date +%Y.%m.%d-%s)

download:
	mkdir -p ./$(WORKING_DIR)
	rsync --rsync-path="sudo rsync" -avz $(SERVER):$(WORKING_DIR) .$(WORKING_DIR)

sync-files:
	# @-git add . && git commit -m "sync $(TODAY)"
	rsync --rsync-path="sudo rsync" --delete -avz .$(WORKING_DIR) $(SERVER):$(WORKING_DIR)

nginx-reload:
	ssh $(SERVER) "sudo nginx -t && sudo nginx -s reload"

upload: sync-files nginx-reload


download-ssl:
	mkdir -p ./$(LET_ENCRYPT_WORKING_DIR)
	rsync --rsync-path="sudo rsync" -avz $(SERVER):$(LET_ENCRYPT_WORKING_DIR) .$(LET_ENCRYPT_WORKING_DIR)
