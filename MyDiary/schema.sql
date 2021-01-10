DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS "posts"
(
    id
    INTEGER
    primary
    key
    autoincrement,
    created
    TIMESTAMP
    default
    CURRENT_TIMESTAMP
    not
    null,
    title
    TEXT
    not
    null,
    content
    TEXT
    not
    null,
    created_by
    int
    constraint
    posts_users_user_id_fk
    references
    users
);

CREATE TABLE IF NOT EXISTS "users"
(
    user_id
    int
    constraint
    users_pk
    primary
    key,
    email
    text
    not
    null,
    password
    text,
    name
    text
    not
    null
);

